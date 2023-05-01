class Lcd:
    def __init__(self, number):
        self.number_matrix = [[], [], []]
        self.set_matrix(number)

    def set_matrix(self, number):
        for letter in number:
            match letter:
                case "0":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append("| |")
                    self.number_matrix[2].append("|_|")
                case "1":
                    self.number_matrix[0].append("   ")
                    self.number_matrix[1].append("  |")
                    self.number_matrix[2].append("  |")
                case "2":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append(" _|")
                    self.number_matrix[2].append("|_ ")
                case "3":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append(" _|")
                    self.number_matrix[2].append(" _|")
                case "4":
                    self.number_matrix[0].append("   ")
                    self.number_matrix[1].append("|_|")
                    self.number_matrix[2].append("  |")
                case "5":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append("|_ ")
                    self.number_matrix[2].append(" _|")
                case "6":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append("|_ ")
                    self.number_matrix[2].append("|_|")
                case "7":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append("  |")
                    self.number_matrix[2].append("  |")
                case "8":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append("|_|")
                    self.number_matrix[2].append("|_|")
                case "9":
                    self.number_matrix[0].append(" _ ")
                    self.number_matrix[1].append("|_|")
                    self.number_matrix[2].append("  |")

    def display(self):
        result = ""
        for elt in self.number_matrix:
            result += " ".join(elt) + "\n"
        return result


