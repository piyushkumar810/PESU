type ChildContent = string | number | string[];

interface LayoutProps {
    children: ChildContent;
}

function Layout({ children }: LayoutProps) {
    return (
        <div>
            {children}
        </div>
    );
}

export default Layout;