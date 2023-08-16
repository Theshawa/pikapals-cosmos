import { gsap } from "gsap";
import { FC, ReactNode, useLayoutEffect, useRef } from "react";
import bg from "../../assets/splash_bg.jpeg";

export const AppLayout: FC<{ children: ReactNode }> = ({ children }) => {
  const splashContainer = useRef<HTMLDivElement>(null);
  const splashTitle = useRef<HTMLDivElement>(null);
  const contentContainer = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
    const ctx = gsap.context(() => {
      const tl = gsap.timeline();
      tl.set(splashContainer.current, { opacity: 0, filter: "blur(20px)" });
      tl.set(splashTitle.current, {
        opacity: 0,
        y: 20,
      });
      tl.set(contentContainer.current, { opacity: 0, filter: "blur(20px)" });
      tl.to(splashContainer.current, {
        opacity: 1,
        filter: "blur(0px)",
        duration: 1.2,
        delay: 1,
      });
      tl.to(splashTitle.current, {
        opacity: 1,
        y: 0,
        duration: 0.8,
        delay: -0.1,
      });
      tl.to(splashContainer.current, {
        opacity: 0,
        filter: "blur(20px)",
        duration: 0.6,
        delay: 2,
      });
      tl.to(contentContainer.current, {
        opacity: 1,
        filter: "blur(0px)",
        duration: 0.3,
      });
      tl.set(splashContainer.current, { display: "none" });
    });

    return () => {
      ctx.revert();
    };
  }, []);

  return (
    <div className="w-full bg-black text-white max-w-[600px] min-h-screen relative mx-auto">
      <div
        ref={splashContainer}
        className="w-full h-full absolute left-0 top-0 z-50 flex p-[20px] bg-cover bg-no-repeat bg-center"
        style={{
          backgroundImage: `url(${bg})`,
        }}
      >
        <h1 ref={splashTitle} className="m-auto">
          Cosmos
        </h1>
      </div>
      <div ref={contentContainer} className="w-full">
        {children}
      </div>
    </div>
  );
};
