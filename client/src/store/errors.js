import { createSlice } from "@reduxjs/toolkit";

const { reducer, actions } = createSlice({
  name: "errors",
  initialState: [],
  reducers: {
    push(state, action) {
      state.push(action.payload);
    },
    pop(state, action) {
      state.pop();
    },
  },
});

export { actions as errorActions };
export { reducer as errorReducer };
