import { useEffect, useState } from "react";
import { Menu } from "antd";
import ReactECharts from "echarts-for-react";


function App() {

    const [current, setCurrent] = useState("1");

    // 保存后端返回的数据
    const [salesData, setSalesData] = useState([]);


    // 页面加载时请求后端
    useEffect(() => {

        fetch("http://127.0.0.1:5000/sales")
            .then(res => res.json())
            .then(data => {

                setSalesData(data);

            })
            .catch(error => {

                console.log(error);

            });

    }, []);



    const items = [
        {
            key: "1",
            label: "数据统计",
        },
        {
            key: "2",
            label: "数据趋势",
        },
        {
            key: "3",
            label: "数据占比",
        },
    ];



    // 柱状图
    const barOption = {

        title: {
            text: "销售数量统计"
        },

        xAxis: {
            type: "category",

            // 数据库里的name
            data: salesData.map(item => item.name)
        },

        yAxis: {
            type: "value"
        },

        series: [
            {
                type: "bar",

                // 数据库里的count
                data: salesData.map(item => item.count)
            }
        ]
    };



    // 折线图
    const lineOption = {

        title: {
            text: "销售趋势"
        },

        xAxis: {
            type: "category",

            data: salesData.map(item => item.name)
        },

        yAxis: {
            type: "value"
        },

        series: [
            {
                type: "line",

                data: salesData.map(item => item.count)
            }
        ]
    };



    // 饼图
    const pieOption = {

        title: {
            text: "销售占比"
        },

        series: [
            {
                type: "pie",

                data: salesData.map(item => {

                    return {

                        value: item.count,

                        name: item.name

                    };

                })
            }
        ]
    };



    function showChart(){

        if(current === "1"){

            return <ReactECharts option={barOption}/>;

        }


        if(current === "2"){

            return <ReactECharts option={lineOption}/>;

        }


        if(current === "3"){

            return <ReactECharts option={pieOption}/>;

        }

    }



    return (

        <div>

            <h1>
                数据库可视化
            </h1>


            <Menu

                mode="horizontal"

                items={items}

                selectedKeys={[current]}

                onClick={(e)=>setCurrent(e.key)}

            />


            {showChart()}


        </div>

    );

}


export default App;
