import { useCallback, useMemo } from "react";

import { TodoItem } from "./todoItem";
import { TodoModel } from "./types";
import { useGetTodosQuery, useAddTodoMutation } from "../api/apiSlice.ts";


export const TodoList = () => {
  const {data: todos = [], isSuccess} = useGetTodosQuery();
  const [addTodo] = useAddTodoMutation();

  const handleAddTodo = useCallback(() => {
    addTodo({
      content: "New Todo item",
      created_at: new Date(Date.now()).toISOString(),
      id: null,
      done_at: null,
    } satisfies TodoModel).unwrap();
  }, [addTodo])

  const sortedTodos = useMemo(() => {
    const sortedTodos = isSuccess ? [...todos] : [];
    sortedTodos.sort((a, b) => {
      return new Date(a.created_at).getTime() - new Date(b.created_at).getTime();
    });
    return sortedTodos;
  }, [todos, isSuccess])


  return (
    <>
      <h2 className={"header-center"}>TODO LIST</h2>
      <button onClick={ handleAddTodo }>Add Todo</button>
      {sortedTodos && sortedTodos.length === 0 && <h4 className={"no-items-header"}>No Todo items</h4>}
      <div className={"todo-list"}>
        { sortedTodos &&
          sortedTodos.length > 0 &&
          sortedTodos.map((todo) => <TodoItem key={ todo.id } item={ todo }/>) }
      </div>
    </>
  );
};
