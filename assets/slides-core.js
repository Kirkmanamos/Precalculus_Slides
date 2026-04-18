/* slides-core.js
 * Shared SlidePresentation engine for HoffMath Classroom HTML decks.
 *
 * Each deck loads this file, then defines its own per-deck section
 * targets and instantiates the presentation:
 *
 *   <script src="assets/slides-core.js"></script>
 *   <script>
 *     SlidesCore.init({
 *       sectionTargets: [
 *         { label: 'Overview', slideId: 'slide-0' },
 *         { label: 'Basics',   slideId: 'slide-1' },
 *         ...
 *       ]
 *     });
 *   </script>
 *
 * The init() helper waits for KaTeX to render (if loaded) and then
 * starts the presentation. Pass sectionTargets: [] to skip section nav.
 */

(function (global) {
    'use strict';

    function renderMath() {
        if (typeof renderMathInElement !== 'function') return;
        renderMathInElement(document.body, {
            delimiters: [
                { left: '\\[', right: '\\]', display: true  },
                { left: '\\(', right: '\\)', display: false }
            ],
            throwOnError: false
        });
    }

    function splitAnnotations() {
        document.querySelectorAll('.step-math').forEach(stepMath => {
            const annotation = stepMath.querySelector('.annotation');
            if (!annotation) return;
            const eqDiv = document.createElement('div');
            eqDiv.className = 'step-eq';
            const before = [];
            for (const node of stepMath.childNodes) {
                if (node === annotation) break;
                before.push(node);
            }
            before.forEach(node => eqDiv.appendChild(node));
            stepMath.insertBefore(eqDiv, annotation);
            stepMath.classList.add('has-annotation');
        });
    }

    class SlidePresentation {
        constructor(options = {}) {
            this.slides = Array.from(document.querySelectorAll('.slide'));
            this.current = 0;
            this.total = this.slides.length;
            this.progressBar = document.getElementById('progressBar');
            this.navDotsEl = document.getElementById('navDots');
            this.clickHint = document.getElementById('clickHint');
            this.sectionTargets = options.sectionTargets || [];
            this._buildNav();
            this._buildSectionNavs();
            this._activate(0);
            this._bindEvents();
        }

        _buildNav() {
            if (!this.navDotsEl) { this.dots = []; return; }
            this.slides.forEach((_, index) => {
                const dot = document.createElement('button');
                dot.className = 'nav-dot';
                dot.setAttribute('aria-label', `Go to slide ${index + 1}`);
                dot.addEventListener('click', event => {
                    event.stopPropagation();
                    this._goTo(index);
                });
                this.navDotsEl.appendChild(dot);
            });
            this.dots = Array.from(this.navDotsEl.querySelectorAll('.nav-dot'));
        }

        _buildSectionNavs() {
            this.sectionButtons = this.sectionTargets
                .map(target => ({ ...target, index: this.slides.findIndex(slide => slide.id === target.slideId) }))
                .filter(target => target.index >= 0)
                .map(target => ({ ...target, buttons: [] }));

            if (this.sectionButtons.length === 0) return;

            this.slides.forEach(slide => {
                const nav = document.createElement('div');
                nav.className = 'slide-section-nav';
                nav.setAttribute('aria-label', 'Section navigation');

                this.sectionButtons.forEach(target => {
                    const button = document.createElement('button');
                    button.className = 'slide-section-chip';
                    button.type = 'button';
                    button.textContent = target.label;
                    button.setAttribute('aria-label', `Jump to ${target.label}`);
                    button.addEventListener('click', event => {
                        event.stopPropagation();
                        this._goTo(target.index);
                    });
                    nav.appendChild(button);
                    target.buttons.push(button);
                });

                slide.appendChild(nav);
            });
        }

        _sync() {
            this.dots.forEach((dot, index) => dot.classList.toggle('active', index === this.current));
            if (this.progressBar) {
                this.progressBar.style.width = ((this.current + 1) / this.total * 100) + '%';
            }
            const activeSection = [...this.sectionButtons].reverse().find(target => this.current >= target.index);
            this.sectionButtons.forEach(target => {
                target.buttons.forEach(button => button.classList.toggle('active', target === activeSection));
            });
            const slide = this.slides[this.current];
            const max = parseInt(slide.dataset.steps || 0, 10);
            const cur = parseInt(slide.dataset.currentStep ?? -1, 10);
            if (this.clickHint) {
                this.clickHint.textContent =
                    cur < max - 1 ? 'click to advance'
                    : this.current < this.total - 1 ? 'click for next slide'
                    : '';
            }
        }

        _activate(index) {
            this.slides[index].classList.add('active');
            this._sync();
        }

        _goTo(index) {
            if (index === this.current) return;
            const out = this.slides[this.current];
            out.classList.add('exit-left');
            out.classList.remove('active');
            setTimeout(() => out.classList.remove('exit-left'), 500);
            this.current = index;
            this.slides[index].classList.add('active');
            this._sync();
        }

        _advanceStep(slide) {
            const max = parseInt(slide.dataset.steps || 0, 10);
            let cur = parseInt(slide.dataset.currentStep ?? -1, 10);
            if (cur < max - 1) {
                cur++;
                slide.dataset.currentStep = cur;
                const step = slide.querySelector(`#${slide.id}-step-${cur}`);
                if (step) {
                    step.classList.add('visible');
                    step.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
                this._sync();
                return true;
            }
            return false;
        }

        _retreatStep(slide) {
            let cur = parseInt(slide.dataset.currentStep ?? -1, 10);
            if (cur < 0) return false;
            slide.querySelector(`#${slide.id}-step-${cur}`)?.classList.remove('visible');
            slide.dataset.currentStep = cur - 1;
            this._sync();
            return true;
        }

        _next() {
            if (!this._advanceStep(this.slides[this.current]) && this.current < this.total - 1) {
                this._goTo(this.current + 1);
            }
        }

        _prev() {
            if (!this._retreatStep(this.slides[this.current]) && this.current > 0) {
                this._goTo(this.current - 1);
            }
        }

        _bindEvents() {
            document.addEventListener('keydown', event => {
                if (['ArrowRight', 'ArrowDown', ' '].includes(event.key)) {
                    event.preventDefault();
                    this._next();
                } else if (['ArrowLeft', 'ArrowUp'].includes(event.key)) {
                    event.preventDefault();
                    this._prev();
                }
            });

            document.addEventListener('click', event => {
                if (!event.target.closest('.nav-dot') && !event.target.closest('.slide-section-nav')) {
                    this._next();
                }
            });

            let touchX = 0;
            document.addEventListener('touchstart', event => {
                touchX = event.touches[0].clientX;
            }, { passive: true });

            document.addEventListener('touchend', event => {
                const delta = event.changedTouches[0].clientX - touchX;
                if (Math.abs(delta) > 50) {
                    delta < 0 ? this._next() : this._prev();
                }
            }, { passive: true });
        }
    }

    function init(options = {}) {
        renderMath();
        splitAnnotations();
        return new SlidePresentation(options);
    }

    global.SlidesCore = {
        SlidePresentation,
        init,
        renderMath,
        splitAnnotations
    };
})(window);
