#!/bin/bash
# extract_stats.sh - per-year summary from monthly_series.csv
# columns: year,month,value
tail -n +2 monthly_series.csv | awk -F, '
{ sum[$1] += $3; n[$1] += 1; if (!($1 in max) || $3 > max[$1]) max[$1] = $3 }
END { for (y in sum) printf "%s %.3f %.3f\n", y, sum[y]/n[y], max[y] }' | sort | sed 's/^\(....\) /\1: mean=/; s/ \([0-9.-]*\)$/ max=\1/' | head -12
