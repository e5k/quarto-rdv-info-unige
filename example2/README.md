# Example 2 - One analysis, three documents

## Open the finished examples

- `_output/slides.html`: one Reveal.js slide, with a figure, table and inline results.
- `_output/manuscript.pdf` and `_output/manuscript.docx`: PDF and Word versions of the same report, with cross-references and bibliography.
- `_output/webpage.html`: a self-contained webpage with expandable Python code.

## Render

Requirements: Quarto 1.8 or later, Python with pandas, Seaborn, Matplotlib, tabulate
and Jupyter, an internet connection, and XeLaTeX for the PDF.

From this folder:

```sh
quarto render --to all
```

If Quarto needs to be pointed to the existing course Python environment on this computer:

```sh
QUARTO_PYTHON=/Users/seb/mambaforge/envs/gis/bin/python quarto render --to all
```

## Render individual sources

```sh
quarto render manuscript.qmd --to all  # PDF and Word
quarto render slides.qmd               # Reveal.js
```

The PDF-only figure setting is scoped under `format.pdf`, so Word uses an
Office-compatible image. The `.qmd` sources contain their own Python blocks, prose and inline expressions,
and share the analysis functions and bibliography. HTML CSS does not style the Word output.

## What is shared?

- `_quarto.yml` is the only YAML configuration file. It holds the bibliography,
  execution settings and render list. Each `.qmd` has a small front matter block
  selecting its format and format-specific options. These blocks are YAML syntax,
  but do not require separate `.yml` files.
- `analysis.py` loads and filters data, draws the Seaborn scatter plot,
  and computes the table of mean compositions. It is imported by all three documents.
- Each `.qmd` contains its Python setup block, prose, inline expressions and calls
  to the plotting and table functions directly. There is no include folder.
- The short import, inline calculations and function calls repeat so each document
  is easy to teach from. Filtering, plotting and group means stay in `analysis.py`. Each `.qmd`
  computes its simple inline values directly from the loaded data.
- `references.bib` is a copy of the course bibliography, with the original `Smith2011` key.

All outputs use Quarto's default appearance. The slide uses a larger canvas to
keep the figure and table readable on a single slide. HTML code is folded for inspection.
`assets/slides.css` preserves figure proportions and reduces table text; `assets/webpage.css`
limits the webpage figure to 620 pixels wide. Both files contain only layout adjustments.

## A two-minute live demonstration

1. Open the three outputs and compare the analytical count, mean, table and plot.
2. Open `webpage.qmd`: show its Python setup block, then the inline expression
   in the sentence immediately below. The figure and table calls are in the same file.
3. In `analysis.py`, change `MIN_SIO2 = 0.0` to `MIN_SIO2 = 58.0`.
4. Run `quarto render --to all` and reload all three outputs.
5. Point out how the figure, table and prose agree. Restore `0.0` and render again.

This example recomputes the shared analysis for each output. It avoids duplicated
analysis logic while keeping the short presentation blocks inside each document;
it does not run the analysis only once. For expensive work,
an upstream script could save shared results for the documents to read.

## Data provenance

Data are loaded directly from the Data Science GitHub repository:
https://raw.githubusercontent.com/ELSTE-Master/Data-Science/main/Data/Smith_glass_post_NYT_data_majors.csv

No dataset is stored in this repository. Rendering requires an internet connection.
`references.bib` is copied from the course bibliography; the original is unchanged.

The CSV contains 1,777 analytical rows before the example's eruption selection.
The demonstration uses three named eruptions to keep the slide legible. Oxide
contents are used as provided, without normalization; `n` counts analytical rows,
not necessarily independent specimens. The plot is descriptive and does not
establish that glass chemistry alone identifies an eruption.

Smith, V. C., Isaia, R., and Pearce, N. J. G. (2011). Tephrostratigraphy and glass
compositions of post-15 kyr Campi Flegrei eruptions: Implications for eruption
history and chronostratigraphic markers. Quaternary Science Reviews, 30, 3638-3660.
https://doi.org/10.1016/j.quascirev.2011.07.012

Quarto references:
- https://quarto.org/docs/computations/inline-code.html

## Simple Python blocks

The scatter plot uses `sns.scatterplot(..., hue="Eruption")`.
The table uses `data.groupby("Eruption")[["SIO2", "K2O"]].mean().round(2)`.
Counts and mean SiO2 are plain variables used directly in the text.
