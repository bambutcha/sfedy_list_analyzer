class ValidationSnils:
    def __init__(self) -> None:
        self.__student_snils = "000-000-00 07"

    @property
    def student_snils(self) -> str:
        return self.__student_snils

    @student_snils.setter
    def student_snils(self, value:str) -> None:
        scr = "".join([i for i in value if i.isdigit()])
        if len(scr)==11:
            self.__student_snils = f"{scr[:3]}-{scr[3:6]}-{scr[6:9]} {scr[9:]}"
        else:
            raise IndexError(f'Эта строка не валидна. В ней {len(scr)} цифр, а должно быть 11')



if __name__=="__main__":
    v = ValidationSnils()
    v.student_snils = "90200160057"
    print(v.student_snils)