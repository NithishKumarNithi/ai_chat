import LoginForm from "./components/forms/LoginForm"

function App() {

  async function handleLoginSubmit(e, user){
    e.preventDefault();
    console.log("login submit is clicked");

    let data = new FormData()

    Object.entries(user).map(([key, value]) => {
      console.log("Key : ", key)
      console.log("Value : ", value)
      data.append(key, value)
    })

    let token = await fetch("http://127.0.0.1:8000/home/login", {
      method: "POST",
      body: data 
    });
    let res = await token.json();
    console.log(res)
    
   
    

  }   

  return (
    <div className="App">
      <LoginForm onSubmit={handleLoginSubmit}/>
    </div>
  );
}

export default App;
