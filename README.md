# mag_source_code

trying_to_launch_w2v - основной скрипт для обучалки модели и подачи на вход корпуса в виде дампа pickle. сейчас с параметром synt_cont для синтаксического алгоритма, можно просто убрать

vocab_manager - чтобы поиграться с моделями. комменты внутри

gensim/~ - скомпиленный ворд2век с синтаксичеким функционалом и проапдейченный для последнего релиза. если не передать параметр synt_cont = 1, то считает как обычно.
"синтаксический алгоритм" на данный момент получает предложение и в качестве целевого слова использует только последнее слово в качестве целевого (легкий хак для модели, обучающейся внутри слова)

все остальное - вспомогательные скрипты для препроцессинга/всяких переделок копруса под нужды моделей
не включает токенизатор kuromoji (он на java, враппер для jython)
