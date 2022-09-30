const { createSlice } = require("@reduxjs/toolkit");

const { reducer, actions } = createSlice({
  name: "session",
  initialState: {
    user: null,
  },
  reducers: {
    updateUser(state, action) {
      state.user = action.payload;
    },
  },
});

export { actions as sessionActions };
export { reducer as sessionReducer };
