# DLV Beautifier

Simple Python script that enhances the output of DLV.

## Get DLV

http://www.dlvsystem.com/

## Usage

Just pipe the output of DLV into the Beautifier:

`dlv {FRONTEND} -silent {OPTIONS} [filename [filename [...]]] | python3 beautifier.py`

If the `silent` option is not set, the header of DLV will be shown as its own answer set.

## What the Beautifier does

- Sorts the atoms by name, ascending
- Puts each atom of each answer set into its own line
- Improves readability by adding spaces
- Hides negative atoms (that start with `-`)
