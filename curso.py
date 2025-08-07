#SISTEMA SIGAA
#classe curso 
class Curso():
    def __init__(self, nome, grau, sigla, carga_horaria_total, descricao = None):
        if isinstance(nome, str):
            if len(nome) >= 10 and len(nome) <= 100:
                self.__nome = nome
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
        ##
        if isinstance(carga_horaria_total, int):
            if carga_horaria_total >= 600:
                self.__carga_horaria_total = carga_horaria_total
            else:
                raise ValueError('Carga_horaria_total deve conter no minimo 600 caracteres')
        else:
            raise TypeError('Carga_horaria_total deve ser interger')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and 10 <= len(valor) <= 100:
            self.__nome = valor
        else:
            raise ValueError('Nome deve ser uma string entre 10 e 100 caracteres')

    @property
    def grau(self):
        return self.__grau

    @grau.setter
    def grau(self, valor):
        if isinstance(valor, str) and 5 <= len(valor) <= 30:
            self.__grau = valor
        else:
            raise ValueError('Grau deve ser uma string entre 5 e 30 caracteres')

    @property
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, valor):
        if isinstance(valor, str) and len(valor) == 3:
            self.__sigla = valor
        else:
            raise ValueError('Sigla deve ser uma string de exatamente 3 caracteres')

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        if isinstance(valor, str) and 0 <= len(valor) <= 500:
            self.__descricao = valor
        else:
            raise ValueError('Descricao deve ser uma string entre 0 e 500 caracteres')

    @property
    def carga_horaria_total(self):
        return self.__carga_horaria_total

    @carga_horaria_total.setter
    def carga_horaria_total(self, valor):
        if isinstance(valor, int) and valor >= 600:
            self.__carga_horaria_total = valor
        else:
            raise ValueError('Carga horária total deve ser um inteiro com no minimo 600 caracteres')
    
    @classmethod
    def cria_curso(cls):
        '''cria uma nova instancia de curso'''
        nome = input('Digite o nome do curso: ')
        sigla = input(f'Digite a sigla do curso {nome}: ')
        grau = input(f'Digite o grau do curso: ')
        hr = int(input('Digite a carga horária total do curso: '))
        desc = input('[OPCIONAL] Digite a descrição do curso: ')
        return cls(nome,grau,sigla,hr,desc)

    def __str__(self):
        '''Metodo de retorno basico'''
        retorno = f'Curso: {self.__nome} | {self.__sigla} \nGrau: {self.__grau}\nCarga horária: {self.__carga_horaria_total}'
        if len(self.__descricao) > 0:
            retorno += f'\nDescrição: {self.__descricao}'
        return retorno

################################################################
cursoA = Curso('Análise e Desen. de Sistemas', 'Tecnologo', 'ADS', 1872)

print(cursoA)