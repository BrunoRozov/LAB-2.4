import random

# Annab suvalise rea numbrid 1-9
class Generator:
    def generate(self, count):
        return [random.randint(1, 9) for _ in range(count)]

# See klass peab võtma sisse 2D listi ja tagastama kõik vajalikud alamlistid:
class Splitter:
    def split(self, matrix):
        result = []
        n = len(matrix)

        # 1. Read
        result.extend(matrix)

        # 2. Veerud
        for i in range(n):
            column = []
            for row in matrix:
                column.append(row[i])
            result.append(column)

        # 3. Peadiagonaal
        main_diag = []
        for i in range(n):
            main_diag.append(matrix[i][i])
        result.append(main_diag)

        # 4. Kõrvaldiagonaal
        other_diag = []
        for i in range(n):
            other_diag.append(matrix[i][n - 1 - i])
        result.append(other_diag)

        return result
    # Ma ei oleks elusees seda mõtlend üksinda välja
    
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

s = Splitter()
print(s.split(matrix))

# Kontrollib ära, kas kõik on oke
class Verifier:
    def verify(self, data):
        target = sum(data[0])

        for group in data:
            if sum(group) != target:
                # Kõik ei ole
                return False
            
        # Kõik on oke
        return True

v = Verifier()
print(v.verify([
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8],
    [2, 9, 4],
    [7, 5, 3],
    [6, 1, 8],
    [2, 5, 8],
    [6, 5, 4]
]))

class MagicsquareGenerator:
    def __init__(self):
        # Võtame kõik ilusasti kokku
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            # loob numero
            nums = self.generator.generate(size * size)

            # Teeb matrix
            matrix = []
            for i in range(size):
                row = nums[i * size:(i + 1) * size]
                matrix.append(row)

            # Split
            parts = self.splitter.split(matrix)

            # Kontrollib
            if self.verifier.verify(parts):
                return matrix