# Markdown Report Generator Action
Report generator that takes multiple .md files from a source and combines them into a single .md file.

## Inputs
### docs-path
**required** \
Path for the documentation files to use to generate the report. \
Default: docs/

### output-path
**required** \
Output path for the report to generate. \
Default: docs/report.md

### blacklist
Comma seperated list of files and directories to ignore during the report's generation. Only the name of the file or directory is needed, not the full path or file extension. \
This list automatically includes the [output-path](#output-path), so there is no need to add it manually. \
Example: file1,file2,dir1

### table-of-content
Index of the page where to generate a table of contents. If not specified, no table will be generated. \
Index starts at ```0```. \
Example: 0

### presentation-page
Content to add as a presentation page at the very beginning of the report.
Example: Lorem Ipsum...

### presentation-placeholders
Comma seperated list of values for the placeholders used in the [presentation-page](#presentation-page). \
The syntax must be ```PLACEHOLDER:VALUE```. \
Example: DATE:01/01/01,STUFF:abc

## Example
See the [example folder](/example) for a folder structure example. \
Also see the [example report](/example/docs/report.md) for an example of a generated report.
