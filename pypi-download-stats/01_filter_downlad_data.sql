/* Detect downloads coming from real users */

SELECT
  details.installer.name,
  details.cpu is NULL as cpu_is_null,
  COUNT(*) as download_count,
FROM
  TABLE_DATE_RANGE(
    [the-psf:pypi.downloads],
    DATE_ADD(CURRENT_TIMESTAMP(), -30, "day"),
    DATE_ADD(CURRENT_TIMESTAMP(), -1, "day")
  )
GROUP BY
  details.installer.name,
  cpu_is_null
ORDER BY
  download_count DESC
