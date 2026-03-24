const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, BorderStyle, WidthType,
  ShadingType, HeadingLevel, PageNumber, PageBreak
} = require("docx");

// ── Color palette ──
const NAVY = "1A365D";
const BLUE = "2563EB";
const GREEN = "16A34A";
const TEAL = "0891B2";
const ORANGE = "D97706";
const RED = "DC2626";
const LIGHT_BLUE = "EFF6FF";
const LIGHT_GREEN = "F0FDF4";
const LIGHT_TEAL = "F0FDFA";
const LIGHT_ORANGE = "FFFBEB";
const LIGHT_RED = "FEF2F2";
const GRAY = "F8FAFC";

// ── Helpers ──
const border = { style: BorderStyle.SINGLE, size: 1, color: "D1D5DB" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0 };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };

function sectionHeader(text, color) {
  return new Paragraph({
    spacing: { before: 300, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: color, space: 4 } },
    children: [
      new TextRun({ text, bold: true, size: 28, font: "Arial", color: color }),
    ],
  });
}

function subHeader(text) {
  return new Paragraph({
    spacing: { before: 200, after: 80 },
    children: [
      new TextRun({ text, bold: true, size: 22, font: "Arial", color: NAVY }),
    ],
  });
}

function identityRow(label, formulas, fillColor, borderColor) {
  return new TableRow({
    children: [
      new TableCell({
        width: { size: 1800, type: WidthType.DXA },
        borders,
        shading: { fill: fillColor, type: ShadingType.CLEAR },
        margins: cellMargins,
        verticalAlign: "center",
        children: [new Paragraph({
          children: [new TextRun({ text: label, bold: true, size: 18, font: "Arial", color: borderColor })],
        })],
      }),
      new TableCell({
        width: { size: 7560, type: WidthType.DXA },
        borders,
        shading: { fill: fillColor, type: ShadingType.CLEAR },
        margins: cellMargins,
        verticalAlign: "center",
        children: formulas.map(f => new Paragraph({
          spacing: { before: 20, after: 20 },
          children: [new TextRun({ text: f, size: 20, font: "Cambria Math" })],
        })),
      }),
    ],
  });
}

function strategyItem(num, text) {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    indent: { left: 360 },
    children: [
      new TextRun({ text: `${num}. `, bold: true, size: 20, font: "Arial", color: BLUE }),
      new TextRun({ text, size: 20, font: "Arial" }),
    ],
  });
}

function cautionBox(text) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    border: {
      left: { style: BorderStyle.SINGLE, size: 12, color: RED, space: 8 },
    },
    indent: { left: 200 },
    shading: { fill: LIGHT_RED, type: ShadingType.CLEAR },
    children: [
      new TextRun({ text: "⚠ CAUTION: ", bold: true, size: 20, font: "Arial", color: RED }),
      new TextRun({ text, size: 20, font: "Arial", color: RED }),
    ],
  });
}

function tipBox(label, text, color, bgColor) {
  return new Paragraph({
    spacing: { before: 100, after: 100 },
    border: {
      left: { style: BorderStyle.SINGLE, size: 12, color: color, space: 8 },
    },
    indent: { left: 200 },
    shading: { fill: bgColor, type: ShadingType.CLEAR },
    children: [
      new TextRun({ text: label + ": ", bold: true, size: 20, font: "Arial", color: color }),
      new TextRun({ text, size: 20, font: "Arial" }),
    ],
  });
}

function guidelineItem(num, text) {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    indent: { left: 360 },
    children: [
      new TextRun({ text: `${num}. `, bold: true, size: 20, font: "Arial", color: TEAL }),
      new TextRun({ text, size: 20, font: "Arial" }),
    ],
  });
}

// ── Build document ──
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Arial", size: 22 } },
    },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 720, right: 1080, bottom: 720, left: 1080 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: NAVY, space: 4 } },
          children: [
            new TextRun({ text: "Precalculus Review — Sections 5.1–5.3", bold: true, size: 18, font: "Arial", color: NAVY }),
          ],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Page ", size: 16, font: "Arial", color: "999999" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 16, font: "Arial", color: "999999" }),
          ],
        })],
      }),
    },
    children: [
      // ── Title ──
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 40 },
        children: [
          new TextRun({ text: "Trig Identities & Equations", bold: true, size: 40, font: "Arial", color: NAVY }),
        ],
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [
          new TextRun({ text: "Sections 5.1–5.3 Quick Reference Sheet", size: 22, font: "Arial", color: "64748B" }),
        ],
      }),

      // ══════════════════════════════════════════
      // SECTION 5.1
      // ══════════════════════════════════════════
      sectionHeader("Section 5.1 — Using Fundamental Identities", BLUE),

      subHeader("Fundamental Identity Families"),

      // Identity table
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [1800, 7560],
        rows: [
          identityRow("PYTHAGOREAN", [
            "sin²θ + cos²θ = 1",
            "1 + tan²θ = sec²θ",
            "1 + cot²θ = csc²θ",
          ], LIGHT_GREEN, GREEN),
          identityRow("RECIPROCAL", [
            "csc θ = 1/sin θ          sec θ = 1/cos θ          cot θ = 1/tan θ",
          ], LIGHT_BLUE, BLUE),
          identityRow("QUOTIENT", [
            "tan θ = sin θ / cos θ          cot θ = cos θ / sin θ",
          ], LIGHT_TEAL, TEAL),
          identityRow("EVEN / ODD", [
            "cos(−θ) = cos θ     (even)",
            "sin(−θ) = −sin θ     (odd)",
            "tan(−θ) = −tan θ     (odd)",
          ], LIGHT_ORANGE, ORANGE),
        ],
      }),

      subHeader("Simplification Strategies"),
      strategyItem(1, "Factor out a common term"),
      strategyItem(2, "Apply a Pythagorean identity"),
      strategyItem(3, "Rewrite everything in sine and cosine"),
      strategyItem(4, "Find a common denominator"),
      strategyItem(5, "Factor a difference of squares"),
      strategyItem(6, "Multiply by the conjugate"),

      tipBox("GOAL", "Reduce to fewer trig functions, eliminate fractions, or match a target form.", BLUE, LIGHT_BLUE),

      // ══════════════════════════════════════════
      // SECTION 5.2
      // ══════════════════════════════════════════
      sectionHeader("Section 5.2 — Verifying Trig Identities", TEAL),

      subHeader("Guidelines for Verifying"),
      guidelineItem(1, "Work with the more complicated side"),
      guidelineItem(2, "Convert everything to sine and cosine"),
      guidelineItem(3, "Factor expressions"),
      guidelineItem(4, "Find a common denominator"),
      guidelineItem(5, "Multiply by the conjugate"),
      guidelineItem(6, "Apply Pythagorean identities"),
      guidelineItem(7, "Work each side separately toward a common middle"),

      cautionBox("Never cross the equal sign! Do not add to both sides, multiply both sides, or square both sides."),

      tipBox("REMEMBER", "An identity is a statement that is true for ALL values in the domain. You prove it by transforming one side into the other.", TEAL, LIGHT_TEAL),

      // ══════════════════════════════════════════
      // SECTION 5.3
      // ══════════════════════════════════════════
      sectionHeader("Section 5.3 — Solving Trig Equations", GREEN),

      subHeader("Key Strategies"),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        indent: { left: 360 },
        children: [
          new TextRun({ text: "1. ", bold: true, size: 20, font: "Arial", color: GREEN }),
          new TextRun({ text: "Isolate the trig function (treat it like solving for ", size: 20, font: "Arial" }),
          new TextRun({ text: "x", italics: true, size: 20, font: "Arial" }),
          new TextRun({ text: " in algebra)", size: 20, font: "Arial" }),
        ],
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        indent: { left: 360 },
        children: [
          new TextRun({ text: "2. ", bold: true, size: 20, font: "Arial", color: GREEN }),
          new TextRun({ text: "Factor — ", bold: true, size: 20, font: "Arial" }),
          new TextRun({ text: "never divide both sides by a trig function", size: 20, font: "Arial" }),
        ],
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        indent: { left: 360 },
        children: [
          new TextRun({ text: "3. ", bold: true, size: 20, font: "Arial", color: GREEN }),
          new TextRun({ text: "Use Pythagorean identities to rewrite in one trig function", size: 20, font: "Arial" }),
        ],
      }),
      new Paragraph({
        spacing: { before: 40, after: 40 },
        indent: { left: 360 },
        children: [
          new TextRun({ text: "4. ", bold: true, size: 20, font: "Arial", color: GREEN }),
          new TextRun({ text: "Use the unit circle for exact values", size: 20, font: "Arial" }),
        ],
      }),

      cautionBox("Never divide both sides by a trig function — you will lose solutions! Factor instead."),

      subHeader("Restricted Domain vs. General Solutions"),

      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [4680, 4680],
        rows: [
          new TableRow({
            children: [
              new TableCell({
                width: { size: 4680, type: WidthType.DXA },
                borders,
                shading: { fill: LIGHT_GREEN, type: ShadingType.CLEAR },
                margins: { top: 80, bottom: 80, left: 120, right: 120 },
                children: [
                  new Paragraph({
                    spacing: { after: 60 },
                    children: [new TextRun({ text: "Restricted Domain [0, 2π)", bold: true, size: 20, font: "Arial", color: GREEN })],
                  }),
                  new Paragraph({
                    children: [new TextRun({ text: "List only the angles that fall within the given interval.", size: 18, font: "Arial" })],
                  }),
                  new Paragraph({
                    spacing: { before: 60 },
                    children: [
                      new TextRun({ text: "Example: ", italics: true, size: 18, font: "Arial", color: "64748B" }),
                      new TextRun({ text: "cos θ = ½  →  θ = π/3, 5π/3", size: 18, font: "Cambria Math" }),
                    ],
                  }),
                ],
              }),
              new TableCell({
                width: { size: 4680, type: WidthType.DXA },
                borders,
                shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
                margins: { top: 80, bottom: 80, left: 120, right: 120 },
                children: [
                  new Paragraph({
                    spacing: { after: 60 },
                    children: [new TextRun({ text: "General Solution (all solutions)", bold: true, size: 20, font: "Arial", color: BLUE })],
                  }),
                  new Paragraph({
                    children: [new TextRun({ text: "Add + 2πn (or + πn for tan/cot) where n is any integer.", size: 18, font: "Arial" })],
                  }),
                  new Paragraph({
                    spacing: { before: 60 },
                    children: [
                      new TextRun({ text: "Example: ", italics: true, size: 18, font: "Arial", color: "64748B" }),
                      new TextRun({ text: "cos θ = ½  →  θ = π/3 + 2πn, 5π/3 + 2πn", size: 18, font: "Cambria Math" }),
                    ],
                  }),
                ],
              }),
            ],
          }),
        ],
      }),

      // ── Spacer + closing tip ──
      new Paragraph({ spacing: { before: 200 } }),
      tipBox("PRO TIP", "When in doubt: rewrite in sin and cos, look for a Pythagorean identity, and factor!", NAVY, GRAY),
    ],
  }],
});

// ── Write file ──
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/Users/kirkmanamos/Documents/GitHub/precalculus_slides/5.1-5.3-review-handout.docx", buffer);
  console.log("✅ Handout created: 5.1-5.3-review-handout.docx");
});
