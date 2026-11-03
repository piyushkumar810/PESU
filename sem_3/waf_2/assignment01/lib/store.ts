export type Feedback = {
  id: string;
  userId: string;
  rating: number;
  comment: string;
  status: "pending" | "approved";
  createdAt: string;
};

const globalStore = globalThis as typeof globalThis & {
  feedbackData?: Feedback[];
};

export const feedbackData =
  globalStore.feedbackData ??
  (globalStore.feedbackData = []);