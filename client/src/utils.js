export function setSession(sess_key, sess_value) {
  window.sessionStorage.setItem(sess_key, sess_value);
}

export function getSession(sess_key) {
  return window.sessionStorage.getItem(sess_key);
}

export function removeSession(sess_key) {
  window.sessionStorage.removeItem(sess_key);
}

export function deleteAllSession() {
  window.sessionStorage.clear();
}

export async function verifyToken(token) {
  const authToken = token ? token : getSession("authToken");

  if (!authToken) {
    throw Error("Token is missing");
  }

  let verifyUser = await fetch("http://127.0.0.1:8000/home/verify", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${authToken}`,
    },
  });

  if (!verifyUser) {
    throw Error("Invalid verify url");
  }

  let user = await verifyUser.json();

  if (!user) {
    throw Error("user not found");
  }

  return user;
}
