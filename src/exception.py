import sys
from src.logger import logging

class CustomException(Exception):
    def __init__(self,message,error_detail:sys):
        super().__init__(message)
        self.error_detail=error_detail

        self.info_message=self.get_detailed_info(error_detail)

    def get_detailed_info(self,error_detail:sys):
        _,_,exc_tb=error_detail.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        line_number=exc_tb.tb_lineno
        error_message=exc_tb.tb_frame.f_code.co_name
        return (
            f"Error occurred in file [{file_name}], "
            f"in function [{error_message}], "
            f"at line number [{line_number}]"
        )

    def __str__(self):
        return self.info_message

if __name__=="__main__":
    try:
        raise Exception("Something went wrong")
    except Exception as e:
        logging.info(e,exc_info=True)
        raise CustomException(e,sys)