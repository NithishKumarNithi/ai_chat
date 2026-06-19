import { useState, useEffect } from "react";
import { useParams } from "react-router";
import { getSession } from "../utils";

export default function Dashboard() {
  let [userInfo, setUserInfo] = useState({});
  let { userId } = useParams();

  useEffect(() => {
    let authToken = getSession("authToken");

    if (!authToken) throw Error("Token is Missing");

    async function getUserData() {
      let userData = await fetch(`http://127.0.0.1:8000/users/${userId}`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${authToken}`,
        },
      });

      let userSettings = await fetch(
        `http://127.0.0.1:8000/users/${userId}/settings`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${authToken}`,
          },
        },
      );

      let userInfoRes = await userData.json();
      let userSettingsRes = await userSettings.json();

      if (!userInfoRes || !userSettingsRes) {
        throw Error("Invalid User Details");
      }
      console.log({ ...userInfoRes, ...userSettingsRes });
      setUserInfo({ ...userInfoRes, ...userSettingsRes });
    }
    getUserData();
  }, [userId]);

  return (
    <>
      <h1>Dashboard for user </h1>
      <p>UserName : {userInfo.name ? userInfo.name : "-"}</p>
      <p>Email : {userInfo.email ? userInfo.email : "-"}</p>

      <h2>User Settings </h2>

      <p>Provider : {userInfo.settings ? userInfo.settings.provider : "-"}</p>
      <p>Model : {userInfo.settings ? userInfo.settings.models : "-"}</p>
    </>
  );
}
