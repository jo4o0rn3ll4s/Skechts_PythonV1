from tinydb import TinyDB, Query

DB_PATH = 'db.json'


class Service:
    def __init__(self):
        self.db = TinyDB(DB_PATH)


class Aluno(Service):
    def __init__(self):
        super().__init__()
        self.alunos = self.db.table('alunos')

    def insert(self, nome, renach, categorias, total):
        self.alunos.insert({
            'name': nome,
            'renach': renach,
            'categories': categorias,
            'total_instalment': int(total),
            'paid_instalment': 0,
            'status': 'matriculado'
        })

    def read(self):
        return self.alunos.all()


aluno_service = Aluno()
