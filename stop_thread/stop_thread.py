"""Define stop_thread."""
import ctypes

from logzero import logger


def stop_thread(ident: int):
    """Stop/interrupt a thread with ident.

    Args:
        ident: thread's id, can be obtained by
                 threading.current_thread().ident
                 or int(PyQt5.QtCore.QThread.currentThreadId())

    Very often you'd follow stop_thread(ident) up with:
        thread.quit()
        thread.wait()
    to properly terminate the thread, and possibley other clean-ups (e.g., worker.deleteLater())

    """
    i_error = ctypes.py_object(InterruptedError)

    # if user clicks stop before doing anything
    try:
        tid = ctypes.c_long(ident)
    except Exception as exc:
        logger.error("Cant convert ident to ctypes.c_long: %s", exc)
        return

    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, i_error)

    if res == 0:
        # raise ValueError("invalid thread id")
        logger.error("invalid thread ident: thread probrbaly already stopped")
    elif res == 1:
        logger.info("thread %s interrupted", ident)
        # self.thread.quit()
        # self.worker.deleteLater()
    elif res > 1:
        # we are in trouble
        # call it again with None to revert the effect
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)

        # catch this if necessary and decide what to do
        raise Exception("PyThreadState_SetAsyncExc failed")
