#SISTEMA SIGAA
#classe curso 
class Curso():
    def __init__(self, nome, grau, sigla, carga_horaria_total, descricao = None):
        if isinstance(nome, str):
            if len(nome) >= 10 and len(nome) <= 100:
                self.__nome == nome
            else:
                raise ValueError('Nome deve ter de 10 a 100 caracteres')
        else:
            raise TypeError('Nome deve ser string')
        ##
        if isinstance(grau,str):
            if len(grau) >= 5 and len(grau) <= 30:
                self.__grau = grau
            else:
                raise ValueError('Grau deve ter de 5 a 30 caracteres')
        else:
            raise TypeError('Grau deve ser string')
        ##
        if isinstance(sigla, str):
            if len(sigla) == 3:
                self.__sigla = sigla
            else:
                raise ValueError('Sigla deve ter 3 caracteres')
        else:
            raise TypeError('Sigla deve ser string')
        ##
        if descricao != None and isinstance(descricao,str):
            if len(descricao) >= 0 and len(descricao) <= 500:
                self.__descricao = descricao
            else:
                raise ValueError('Descricao deve ter de 0 a 500 caracteres')
        else:
            self.__descricao = ''
            raise TypeError('[ATRIBUTO OPCIONAL] descricao deve ser string')
        ##
        if isinstance(carga_horaria_total, int):
            if carga_horaria_total >= 600:
                self.__carga_horaria_total = carga_horaria_total
            else:
                raise ValueError('Carga_horaria_total deve conter no minimo 600 caracteres')
        else:
            raise TypeError('Carga_horaria_total deve ser interger')

    def __str__(self):
        