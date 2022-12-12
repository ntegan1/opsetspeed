import { useEffect, useRef, useState } from "react"
function useInterval(callback, delay) {
  const savedCallback = useRef();

  // Remember the latest callback.
  useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  // Set up the interval.
  useEffect(() => {
    function tick() {
      savedCallback.current();
    }
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
}


function Nav() {
  const c = "bg-nord1 flex items-center justify-between"
  const clinkalll = " text-nord5 hover:bg-nord5 hover:text-nord0 py-1 px-2 "
  const clinkhome = " text-nord5 bg-nord10  py-1 px-2 "
  return (
    <div className={c}>
      <div className="flex items-center">
      <p className={clinkhome}>Home</p>
      <p className={clinkalll}>Set Speed</p>
      </div>
    </div>
    
  )
}
function Slider() {
  const url = "http://192.168.1.122:5000"
  const vmin = 0
  const vmax = 28
  const [value, setValue] = useState(vmax)
  //const int_loop = () => { sendv(value); }
  //const onclick = (e) => {setValue(vmax); sendv(vmax) }
  //const onchange = (e) => {const f = e.target.valueAsNumber; setValue(f); sendv(f)}
  //const [done, setDone] = useState(true)
  //const sendalways = (v) => {
  //  try {
  //    fetch(url + "/control/0/" + v, {cache: "no-store", mode:"no-cors", method: "GET", keepalive: true}).then(() => {
  //      setDone(true)
  //    }).catch((e) => {
  //      setDone(true)
  //    })
  //  }
  //  catch (e) {
  //    setDone(true)
  //  }
  //}
  //const sendv = (v) => {
  //  // only send if done
  //  if (!done) { console.log("wait"); return }
  //  setDone(false)
  //  sendalways(v)
  //}
  const c = "[&::-webkit-slider-thumb]:bg-nord8 [&::-webkit-slider-thumb]:w-12 [&::-webkit-slider-thumb]:h-12 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:[appearance:none] [&::-webkit-slider-thumb]:[-webkit-appearance:none] [-webkit-user-select:none] -translate-x-[134px] translate-y-[134px] -rotate-90 h-[32px] w-[300px] bg-gray-700 rounded-lg appearance-none cursor-pointer "
  //useInterval(int_loop, 200)
  useEffect(() => {
    //sendalways(vmax)
    console.log("reload")
    return () => {
      //sendalways(vmax)
      console.log("unmount")
    }
  }, [])
  return (
    <>
      <div className="h-[300px] w-[32px] mt-4">
        <input type="range" step="1" defaultValue={vmax} min={vmin} max={vmax} className={c} />
      </div>
    </>
  )
  //return (
  //  <>
  //    <div className="h-[300px] w-[32px] mt-4">
  //      <input type="range" step="1" onChange={onchange} value={value} min={vmin} max={vmax} className={c} />
  //    </div>
  //    <p className="text-xl font-bold mt-2">{value}</p>
  //    <button onClick={onclick} className={"font-bold mt-4 w-64 h-24 rounded-3xl" + ((value == vmax) ? " bg-nord8 " : " bg-nord6 ")}>
  //      <p className="text-nord1 text-2xl">reset</p>
  //    </button>
  //  </>
  //)
}
function App() {
  const title = "manual set speed"
  return (
  <>
    <Nav />
    <div className="text-nord5 w-full mt-3 flex flex-col items-center justify-between">
      <h1 className="text-4xl">{title}</h1>
      <div className="flex flex-col items-center">
        <p>slider</p>
        <Slider />
      </div>
    </div>
  </>
  );
}

export default App;
