import { RouterProvider } from "react-router-dom";
import { AppLayout } from "./modules/layout";
import { router } from "./router";

function App() {
  return (
    <AppLayout>
      <RouterProvider router={router} />
    </AppLayout>
  );
}

export default App;
