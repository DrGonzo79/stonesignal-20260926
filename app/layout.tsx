import type {Metadata} from "next";
import "./globals.css";
export const metadata:Metadata={title:"StoneSignal — lab-grown ring quote check",description:"A fictional quote-audit workflow for lab-grown engagement ring buyers."};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body>{children}</body></html>}
