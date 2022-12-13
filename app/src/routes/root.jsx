import { Link, Outlet } from "react-router-dom"
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
export default function Root() {
  return (
    <>
      <Nav />
      <Outlet />
    </>
  )
}
