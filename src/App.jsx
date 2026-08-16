
import { useState } from "react";
import { Menu } from "antd";
import ReactECharts from "echarts-for-react";


function App() {

    const [current, setCurrent] = useState("1");


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
            text: "数据统计"
        },
        xAxis: {
            type: "category",
            data: ["A", "B", "C", "D"]
        },
        yAxis: {
            type: "value"
        },
        series: [
            {
                data: [10, 20, 30, 40],
                type: "bar"
            }
        ]
    };


    // 折线图
    const lineOption = {
        title: {
            text: "数据趋势"
        },
        xAxis: {
            type: "category",
            data: ["周一", "周二", "周三", "周四"]
        },
        yAxis: {
            type: "value"
        },
        series: [
            {
                data: [20, 35, 25, 50],
                type: "line"
            }
        ]
    };


    // 饼图
    const pieOption = {
        title: {
            text: "数据占比"
        },
        series: [
            {
                type: "pie",
                data: [
                    {
                        value: 40,
                        name: "A"
                    },
                    {
                        value: 30,
                        name: "B"
                    },
                    {
                        value: 20,
                        name: "C"
                    }
                ]
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