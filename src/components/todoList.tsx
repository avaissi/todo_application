import { useCallback, useEffect, useMemo } from "react";

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
      <button onClick={ handleAddTodo }>Add Todo</button>
      <div>
        { sortedTodos &&
          sortedTodos.length > 0 &&
          sortedTodos.map((todo) => <TodoItem key={ todo.id } item={ todo }/>) }
      </div>
    </>
  );
};
