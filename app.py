import streamlit as st

st.title('To-do App')

# (할일 + 했는지 여부) 객체로 관리하기 위해 만든 클래스
class Todo:
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done

    def set_done(self, done: bool):
        self.__done = done

    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'

    # 객체가 리스트 안에 있을 때 리스트 안의 요소들을 출력하려면 __repr__을 사용해야 함. __str__은 안 나옴.
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'

        # __repr__은 eval()로 다시 객체로 바꿀 수 있는 문자열 형태로 작성하는 게 원칙이다.
        # return f'Todo(task={self.__task!r}, done="{self.__done}")'      # 큰따옴표 대신 {!r}을 써줘도 된다.

# __repr__ 심화 설명
# todo = Todo('숙제하기')
# print(id(todo))
# print(Todo(task='똘이 밥 주기', done=True))          # __repr__에는 이런 식으로 작성하는 것이 원칙.
# todo2 = eval(repr(todo))                            # 생성된 객체를 이용해서 다시 새로운 객체를 만들 수 있다.
# print(id(todo2))                                    # 위의 생성된 todo를 이용해서 다시 만들었는데, 주소값이 다르게 나온다.

# Todo 객체를 list에 쌓는 용도의 함수(새로 추가할 할일을 작성하면 실행되는 함수)
def add_todo():
    print(f'함수가 호출될 때 주머니에 담긴 값: {st.session_state.new_task}')
    todo = Todo(st.session_state.new_task)
    print(f'할일 추가 후 객체의 상태: {todo}')
    # print(todo)
    st.session_state.todos.append(todo)             # todos에 todo 추가
    # print(st.session_state.todos)                   # list를 출력하면 __str__은 주소값, __repr__은 Todo 객체의 문자열로 구성되어 나옴.
    st.session_state.new_task = ""                  # 할일을 추가한 뒤 엔터를 치면 입력창의 글자가 지워짐.

def toggle_done(index: int):
    todo_ = st.session_state.todos[index]            # 받은 index의 todo를 가져옴.
    todo_.set_done(not todo_.get_done())              # 누를 때마다 기존의 값을 반대로 뒤집어줌.


# todos(todo 객체를 담을 리스트를 초기화)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장된다. (session_state에 새로운 키 초기화 알아서 해줌)
st.text_input('새로운 할일 추가', key='new_task', on_change=add_todo)      # on_change: input 창에 내용을 작성하고 엔터를 치면 add_todo라는 함수를 호출하겠다는 의미.
                                        # new_task: 양방향 바인딩. new_task로 받고, new_task를 다시 화면에 보여줌. 고로 빈 문자열로 위에서 초기화가 됐으니 그 다음에 실행될 때는 빈 문자열을 입력창에 출력해준다.

if st.session_state.todos:                          # todos에 무언가 들어있느냐?
    for i, todo in enumerate(st.session_state.todos):
        # st.write(f'{i}번째 todo => {todo}')
        col1, col2 = st.columns([0.1, 0.9])         # 화면을 이분할해줌. (0.1:0.9로)
        col1.checkbox(f'{i + 1}', value=todo.get_done(), key=f'done_{i}', on_change=toggle_done, args=(i,))     # args=(i,)하면 index가 toggle_done으로 넘어감.
        col2.markdown(f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task())

else:
    st.info('할일을 추가해 보세요.')

