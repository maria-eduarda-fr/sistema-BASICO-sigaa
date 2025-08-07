from datetime import date, datetime
from curso import Curso

class Disciplina:
    def __init__(self, nome, ementa, carga_horaria, data_fim, referencias, sigla = None):
        #cod autogerado
        if isinstance(nome, str):
            if len(nome) >= 5 and len(nome) <= 50:
                self.__nome = nome
            else:
                raise ValueError('Nome deve ter de 5 a 50 caracteres')
        else:
            raise TypeError('Nome deve ser string')
        ##
        if isinstance(ementa, str):
            if len(ementa) >= 30 and len(ementa) <= 300:
                self.__ementa = ementa
            else:
                raise ValueError('Ementa deve ter de 30 a 300 caracteres')
        else:
            raise TypeError('Ementa deve ser uma string')
        ##
        if isinstance(carga_horaria, int):
            if carga_horaria >= 20:
                self.__carga_horaria = carga_horaria
            else:
                raise ValueError('Carga horária tem valor mínimo de 20 horas')
        else:
            raise TypeError('Carga horária deve ser integer')
        ##
        self.__data_inicio = date.today().strftime('%d-%m-%Y')
        ##
        if isinstance(data_fim, str):
            #data_fim deve ser uma string no formato 'dd-mm-aaaa'
            try:
                datetime.strptime(data_fim, '%d-%m-%Y')
                if datetime.strptime(data_fim, '%d-%m-%Y') > datetime.now():
                    self.__data_fim = data_fim
                else:
                    raise ValueError('Data de fim não pode ser anterior à data atual')
            except ValueError:
                raise ValueError('Data de fim deve estar no formato dd-mm-aaaa')
        else:
            raise TypeError('Data de fim deve ser string')
        ##
        if isinstance(referencias, str):
            if len(referencias) >= 50 and len(referencias) <= 500:
                self.__referencias = referencias
            else:
                raise ValueError('Referências devem ter de 50 a 500 caracteres')    
        else:
            raise TypeError('Referências devem ser string')
        ##
        if sigla is not None:
            if isinstance(sigla, str):
                if len(sigla) >= 3 and len(sigla) <= 10:
                    self.__sigla = sigla
                else:
                    raise ValueError('Sigla deve ter de 3 a 10 caracteres')
            else:
                raise TypeError('Sigla deve ser string')
            
    @property
    def nome(self):
        return self.__nome  
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and 5 <= len(valor) <= 50:
            self.__nome = valor
        else:
            raise ValueError('Nome deve ser uma string entre 5 e 50 caracteres')    
        
    @property
    def ementa(self):
        return self.__ementa    
    @ementa.setter
    def ementa(self, valor):
        if isinstance(valor, str) and 30 <= len(valor) <= 300:
            self.__ementa = valor
        else:
            raise ValueError('Ementa deve ser uma string entre 30 e 300 caracteres')    
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, valor):
        if isinstance(valor, int) and valor >= 20:
            self.__carga_horaria = valor
        else:
            raise ValueError('Carga horária deve ser um inteiro maior ou igual a 20')
    
    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @property
    def data_fim(self):
        return self.__data_fim
    @data_fim.setter
    def data_fim(self, valor):
        if isinstance(valor, str):
            try:
                datetime.strptime(valor, '%d-%m-%Y')
                if datetime.strptime(valor, '%d-%m-%Y') > datetime.now():
                    self.__data_fim = valor
                else:
                    raise ValueError('Data de fim não pode ser anterior à data atual')
            except ValueError:
                raise ValueError('Data de fim deve estar no formato dd-mm-aaaa')
        else:
            raise TypeError('Data de fim deve ser string')  
    
    @property
    def referencias(self):
        return self.__referencias   
    @referencias.setter
    def referencias(self, valor):   
        if isinstance(valor, str) and 50 <= len(valor) <= 500:
            self.__referencias = valor
        else:
            raise ValueError('Referências devem ser uma string entre 50 e 500 caracteres')
        
    @classmethod
    def criar_disciplina(cls):
        '''cria uma nova instancia de disciplina'''
        nome = input('Digite o nome da disciplina: ')
        ementa = input('Digite a ementa da disciplina: ')
        carga_horaria = int(input('Digite a carga horária da disciplina (mínimo 20 horas): '))
        data_fim = input('Digite a data de fim da disciplina (dd-mm-aaaa): ')
        referencias = input('Digite as referências da disciplina: ')
        sigla = input('[OPCIONAL]Digite a sigla da disciplina: ')
        return cls(nome, ementa, carga_horaria, data_fim, referencias, sigla)
    