export interface TodoModel {
  id: string | null;
  content: string;
  created_at: string;
  done_at?: string | null;
}

export type Todo = {
  id: string;
  content: string;
  createdAt: Date;
  doneAt?: Date;
}
