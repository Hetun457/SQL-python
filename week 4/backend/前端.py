import {useState} from "react";


function App() {

    // 保存第一个输入框的内容
    const [input1, setInput1] = useState("");


    // 点击按钮后发送数据
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


    return (
        <div>

            <h1>React Flask Task</h1>


            <input
                placeholder="第一个输入框"
                onChange={(e) => setInput1(e.target.value)}
            >


            <br />


            <input
                placeholder="第二个输入框"
            >


            <br />


            <input
                placeholder="第三个输入框"
            >


            <br />


            <button onClick={sendData}>
                发送
            <button>


            <button>
                第二个按钮
            <button>


        </div>
    );

}


export default App;
