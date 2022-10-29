import { createSlice } from "@reduxjs/toolkit";

const { reducer, actions } = createSlice({
  name: 'watched',
  initialState: {
    items: [],
  },
  reducers: {
    push(state, action) {
      state.items.push(action.payload);
    },
    pop(state) {
      if (state.items.length) {
        state.items.shift();
      }
    },
  },
});

export { actions as watchedActions };
export { reducer as watchedReducer };