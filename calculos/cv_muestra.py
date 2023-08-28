

from calculos.media import media
from calculos.muestral_standard_deviation import desvio

cv = desvio / media
cv = cv.round(cv, 3)