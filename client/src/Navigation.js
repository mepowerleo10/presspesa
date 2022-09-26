import { useState } from "react";
import { useNavigate } from "react-router-dom";

export const Navigation = () => {
  const navigate = useNavigate();
  const [redirectsHandled, setRedirectsHandled] = useState(false);
};
