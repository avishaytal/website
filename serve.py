#!/usr/bin/env python3
"""
Simple Jekyll development server for debugging
Processes Jekyll files and serves them locally
"""

import http.server
import socketserver
import os
import re
import yaml
from pathlib import Path

class JekyllHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle Jekyll processing
        if self.path == '/' or self.path == '/index.html':
            self.path = '/index.md'
            self.process_jekyll_file()
        elif self.path.endswith('.md'):
            self.process_jekyll_file()
        else:
            super().do_GET()
    
    def process_jekyll_file(self):
        try:
            # Read the markdown file
            file_path = self.path.lstrip('/')
            if not os.path.exists(file_path):
                self.send_error(404, "File not found")
                return
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process front matter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = parts[1]
                    markdown_content = parts[2]
                    
                    # Parse front matter
                    try:
                        fm_data = yaml.safe_load(front_matter)
                        layout = fm_data.get('layout', 'default')
                    except:
                        layout = 'default'
                else:
                    markdown_content = content
                    layout = 'default'
            else:
                markdown_content = content
                layout = 'default'
            
            # Convert markdown to HTML (simple conversion)
            html_content = self.markdown_to_html(markdown_content)
            
            # Load layout
            layout_path = f'_layouts/{layout}.html'
            if os.path.exists(layout_path):
                with open(layout_path, 'r', encoding='utf-8') as f:
                    layout_content = f.read()
                
                # Replace content placeholder
                html_content = layout_content.replace('{{ content }}', html_content)
                
                # Replace site variables
                html_content = html_content.replace('{{ site.title }}', 'Avishay Tal')
                html_content = html_content.replace('{{ site.author.name }}', 'Avishay Tal')
                html_content = html_content.replace('{{ site.description }}', 'Avishay Tal, Associate Professor at UC Berkeley EECS')
                
                # Replace relative URLs
                html_content = html_content.replace('{{ \'/', '/')
                html_content = html_content.replace('| relative_url }}', '')
                
                # Remove Jekyll tags we can't process
                html_content = re.sub(r'{% .*? %}', '', html_content)
            else:
                # Fallback to simple HTML
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Avishay Tal</title>
                    <link rel="stylesheet" href="/assets/css/main.css">
                </head>
                <body>
                    <div class="container">
                        {html_content}
                    </div>
                </body>
                </html>
                """
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, f"Error processing file: {str(e)}")
    
    def markdown_to_html(self, markdown):
        """Simple markdown to HTML converter"""
        html = markdown
        
        # Headers
        html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        
        # Bold
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
        
        # Italic
        html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
        
        # Links
        html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
        
        # Lists
        html = re.sub(r'^- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
        html = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
        
        # Paragraphs
        html = re.sub(r'\n\n', '</p><p>', html)
        html = f'<p>{html}</p>'
        
        # Clean up empty paragraphs
        html = re.sub(r'<p></p>', '', html)
        html = re.sub(r'<p><ul>', '<ul>', html)
        html = re.sub(r'</ul></p>', '</ul>', html)
        
        return html

if __name__ == "__main__":
    PORT = 4000
    
    with socketserver.TCPServer(("", PORT), JekyllHandler) as httpd:
        print(f"Jekyll development server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

