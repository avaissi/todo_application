import {
  createApi,
  fetchBaseQuery,
} from "@reduxjs/toolkit/query/react";
import { TodoModel } from "../components/types"

export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:5000",
  }),
  tagTypes: ["Todos"],
  endpoints: (builder) => ({
    getTodos: builder.query<TodoModel[], null>({
      query: () => "/todos",
      providesTags: ["Todos"],
    }),
    markDoneAt: builder.mutation<TodoModel, { todoId: string, doneAt?: Date }>({
      query: ({todoId, doneAt}) => ({
        url: `/todos/${ todoId }`,
        method: "PUT",
        params: {done_at: doneAt?.toISOString()},
      }),
      invalidatesTags: ["Todos"],
    }),
    updateTodo: builder.mutation<TodoModel, TodoModel>({
      query: (todo) => ({
        url: "/todos/",
        method: "PUT",
        body: todo,
      }),
      invalidatesTags: ["Todos"],
    }),
    addTodo: builder.mutation<TodoModel, TodoModel>({
      query: (todo) => ({
        url: "/todos/",
        method: "POST",
        body: todo,
      }),
      invalidatesTags: ["Todos"],
    }),
    deleteTodo: builder.mutation<boolean, string>({
      query: (todoId) => ({
        url: `/todos/${ todoId }`,
        method: "DELETE",
      }),
      invalidatesTags: ["Todos"],
    }),
  }),
});

export const {useGetTodosQuery, useMarkDoneAtMutation, useUpdateTodoMutation, useAddTodoMutation, useDeleteTodoMutation} = apiSlice;
