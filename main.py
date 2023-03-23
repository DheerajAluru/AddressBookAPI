import uvicorn
import os
def main():
    """ main function """
    uvicorn.run(
        "app.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info")
        #log_config=f"{os.getcwd()}/log.ini"



if __name__ == "__main__":
    main()