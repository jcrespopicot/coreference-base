# coding=utf-8
__author__ = 'Rodrigo Agerri <rodrigo.agerri@ehu.es>'
__date__ = '2013-05-03'

# from Freeling dict (P[PDXITR][123][MFCN]P.*')

plural = set(('ellas', 'ellos', 'las', 'les', 'los', 'mías', 'míos', 'nos', 'nosotras', 'nosotros', 'nuestras', 'nuestros', 'os', 'suyas', 'suyos', 'tuyas', 'tuyos', 'ustedes', 'vosotras', 'vosotros', 'vuestras', 'vuestros'))

# from Freeling dict P[PDXITR][123][MFCN]S.*'

singular = set(('conmigo','contigo','él', 'ella', 'la', 'le', 'lo', 'me', 'mía', 'mí', 'mío', 'nuestra', 'nuestro', 'nuestro', 'suya', 'suyo', 'suyo', 'te', 'ti', 'tú', 'tuya', 'tuyo', 'tuyo', 'usted', 'vos', 'vuestra', 'vuestro', 'vuestro', 'yo'))

# from Freeling dict P[PDXITR][123]F.*'

female = set(('ella', 'ellas', 'la', 'las', 'mía', 'mías', 'nosotras', 'nuestra', 'nuestras', 'suyas', 'suya', 'tuyas', 'tuya', 'vosotras', 'vuestras', 'vuestra'))

# from Freeling dict P[PDXITR][123]M.*

male = set(('él', 'ellos', 'lo', 'los', 'mío', 'míos', 'nosotros', 'nuestro', 'nuestros', 'suyos', 'suyo', 'tuyos', 'tuyo', 'vosotros', 'vuestros', 'vuestro'))

# from Freeling dict P[PDXITR][123][CN].*

neutral = set(('conmigo', 'consigo', 'contigo', 'le', 'les', 'lo', 'me', 'mía', 'mío', 'nos', 'nuestro', 'os', 'se', 'sí', 'suyo', 'te', 'ti', 'tú', 'tuyo', 'ustedes', 'usted', 'vos', 'vuestro', 'yo'))

# from Freeling dict P[PDXITR][123].* and manually remove the ones used for inanimate too

animate = set (('contigo', 'él', 'ella', 'ellas', 'ellos', 'le', 'les', 'me', 'mí', 'nos', 'nosotras', 'nosotros', 'os', 'te', 'ti', 'tí', 'ustedes', 'usted', 'vosotras', 'vosotros', 'vos', 'yo'))

# from Freeling dict P[PDXITR][123].* and manually removing the ones used for animate too

inanimate = set(('lo','los'))

animacy_unknown =

# from Freeling dict PI.*

indefinite = set(('algo', 'alguien', 'alguna', 'algunas', 'alguno', 'algunos', 'ambas', 'ambos', 'bastante', 'bastantes', 'cual', 'cualesquiera', 'cualquiera', 'demás', 'demasiada', 'demasiadas', 'demasiado', 'demasiados', 'media', 'medias', 'medio', 'medios', 'misma', 'mismas', 'mismo', 'mismos', 'mucha', 'muchas', 'mucho', 'muchos', 'nada', 'nadie', 'naide', 'ninguna', 'ningunas', 'ninguno', 'ningunos', 'otra', 'otras', 'otro', 'otros', 'poca', 'pocas', 'poco', 'pocos', 'quienesquiera', 'quienquiera', 'tantas', 'tanta', 'tantos', 'tanto', 'todas', 'toda', 'todos', 'todo', 'unas', 'una', 'unos', 'uno', 'varias', 'varios'))

# from Freeling dict PR.*

relative = set(('adonde', 'como', 'cual', 'cuales', 'cuando', 'cuanta', 'cuantas', 'cuanto', 'cuantos', 'cuya', 'cuyas', 'cuyo', 'cuyos', 'donde', 'que', 'quienes', 'quien'))

others = ()

# this set is used to seach for male and female attributes

all = set(plural + singular + female + male + neutral + animate + inanimate + others)