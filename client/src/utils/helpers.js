import { useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { errorsActions } from "src/store";

/* eslint-disable */
export const useEffectAsync = (effect, deps) => {
  const dispatch = useDispatch();
  const ref = useRef();
  useEffect(() => {
    effect()
      .then((result) => ref.current = result)
      .catch((error) => dispatch(errorsActions.push(error.message)));
      
    return () => {
      const result = ref.current;
      if (result) {
        result();
      }
    };
  }, [...deps, dispatch]);
};