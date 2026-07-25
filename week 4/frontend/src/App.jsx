import { useState } from "react";

function App() {

  const [input1, setInput1] = useState("");
const [input2, setInput2] = useState("");
const [input3, setInput3] = useState("");

  function sendData() {

    fetch("http://127.0.0.1:5000/send", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        xxx: input1
      })
    })

    .then(response => response.json())

    .then(data => {
      alert(data.message);
    });

  }

function sendData2() {

    fetch(`http://127.0.0.1:5000/send2?param=${input3}`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            body: input2
        })

    })

    .then(response => response.json())

    .then(data => {
        alert(data.message);
    });

}


  return (
    <div>

      <h1>React Flask Task</h1>


      <input
        placeholder="第一个输入框"
        onChange={(e) => setInput1(e.target.value)}
      />

      <br />


      <input
    placeholder="第二个输入框"
    onChange={(e)=>setInput2(e.target.value)}
      />

      <br />


      <input
    placeholder="第三个输入框"
    onChange={(e)=>setInput3(e.target.value)}
     />

      <br />


      <button onClick={sendData}>
        发送
      </button>


      <button onClick={sendData2}>
    第二个按钮
     </button>


    </div>
  );
}

export default App;