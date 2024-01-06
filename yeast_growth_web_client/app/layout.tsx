import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Yeast cell growth',
  description: 'Web client Created by Adrian Maciejewski',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" style={{"height": "100%"}}>
      <body className={inter.className} style={{"height": "100%"}}>{children}</body>
    </html>
  )
}
