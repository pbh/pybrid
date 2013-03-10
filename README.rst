pybrid
======
A Simple Python/R/SQL Hybrid Reporting Framework.

__doc__
-------
Various methods and objects are available at the top level:

* run() --- run reports with a ReportRunner.
* main() --- run reports with user specified CLI options.
* hooks.* --- pre- and post- hooks for modifying runner.
* filters.* --- filters for limiting reports generated.

Pybrid is meant to be used with other packages, like:
    
hey_dl, hey_rexec, hey_pgsqlexec, hey_april.

