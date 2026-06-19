import { useNavigate } from "react-router";

import LoginForm from "./components/forms/LoginForm";
import { setSession, verifyToken } from "./utils";

function App() {
  let navigation = useNavigate();

  async function handleLoginSubmit(e, user) {
    e.preventDefault();

    let data = new FormData();

    Object.entries(user).forEach(([key, value]) => {
      data.append(key, value);
    });

    let token = await fetch("http://127.0.0.1:8000/home/login", {
      method: "POST",
      body: data,
    });

    if (!token) {
      throw Error("Invalid Request");
    }

    let res = await token.json();
    console.log(res);
    if (res.token) {
      setSession("authToken", res.token);

      let user = await verifyToken(res.token);
      let { user_id } = user.data;
      console.log(user);
      navigation(`/dashboard/user/${user_id}`);
    } else alert(res.detail);
  }

  return (
    <div className="App">
      <LoginForm onSubmit={handleLoginSubmit} />
    </div>
  );
}

export default App;
