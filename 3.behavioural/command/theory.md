
# rather than any request directly executing business logic.
in this design pattern
request is  converted(encapusulated/transforned) to command object
so that
1.The sender of the request does not need to know how the request is handled.

2.You can store, queue, undo, or log the requests.

3.It decouples the object that sends the request from the object that performs it.
and this command object executed by/executing business logic.
# command object contains all the information and it was executed.
