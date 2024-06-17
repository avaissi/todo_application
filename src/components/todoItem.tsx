import React, { useCallback, useState, useRef, useEffect } from "react";

import { TodoModel } from "./types";
import { useMarkDoneAtMutation, useUpdateTodoMutation, useDeleteTodoMutation } from "../api/apiSlice.ts";


interface TodoProps {
  item: TodoModel;
}

export const TodoItem = ({item}: TodoProps) => {
  const inputRef = useRef<HTMLInputElement>(null);

  const [updateTodo] = useUpdateTodoMutation();
  const [deleteTodo] = useDeleteTodoMutation();
  const [markDoneAt] = useMarkDoneAtMutation();

  const [text, setText] = useState(item.content);
  const [isEditing, setIsEditing] = useState(false);
  const [itemClasses, setItemClasses] = useState("todo-item");

  const handleSetEditable = () => {
    setIsEditing(true);
  }

  const handleBlur = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    updateTodo({
      content: e.target.value ?? "",
      created_at: item.created_at,
      id: item.id,
      done_at: item.done_at,
    } satisfies TodoModel).unwrap().then(() => setIsEditing(false));

  }, [item, updateTodo, setIsEditing]);

  const handleContentChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setText(e.target.value);
  }

  const handleMarkDoneChange = () => {
    if (!item.id) {
      return;
    }
    if (!item.done_at) {
      markDoneAt({
        todoId: item.id,
        doneAt: new Date(Date.now()),
      }).unwrap();
    } else {
      markDoneAt({todoId: item.id, doneAt: undefined}).unwrap();
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      e.currentTarget.blur();
    }
  }

  const handleDelete = useCallback(() => {
    if (!item.id) {
      return;
    }
    deleteTodo(item.id).unwrap();
  }, [item.id, deleteTodo])

  useEffect(() => {
    if (isEditing) {
      inputRef.current?.focus();
    }
  }, [isEditing])

  useEffect(() => {
    if (item.done_at) {
      setItemClasses("todo-item strikethrough")
    } else {
      setItemClasses("todo-item")
    }
  }, [item.done_at, setItemClasses])

  return (
    <div className={"todo-item"}>
      <input type={ "checkbox" } checked={ !!item.done_at } onChange={ handleMarkDoneChange }/>
      <div onDoubleClick={ handleSetEditable }>
        { isEditing ? (
          <input
            ref={ inputRef }
            type="text"
            value={ text }
            onChange={ handleContentChange }
            onSubmit={ handleBlur }
            onBlur={ handleBlur }
            onKeyDown={ handleKeyDown }
          />
        ) : (
          <span className={itemClasses}>{ text }</span>
        ) }
      </div>
      <button onClick={ handleDelete }>X</button>
    </div>
  )
};
