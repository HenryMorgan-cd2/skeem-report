# READ ME

to compile run `./bin/build.sh` from the root directory.
to compile on file change run `./bin/watch.sh` from the root directory. NOTE: you must install inotify-tools with `sudo apt install inotify-tools`

## Citations

[http://www.citationmachine.net]

To make a citation, first add the citation to the `references.bib` file. use the standard bibtex format
Then reference it using `[@referenceName]` for a standard citation. or if you want to include the name within the text then forego the brackets.

```
Its true! [@reference]   =>   Its true (Person Name, 2018)

@reference says its true    =>   Person Name (2018) says its true
```

## Definition Lists

The blank like is required

```
Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b
```

## Multi column Lists

\begin{multicols}{3}
\begin{itemize}
\item item 1
\item item 2
\item item 3
\item item 4
\item item 5
\item item 6
\end{itemize}
\end{multicols}
