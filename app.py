from flask import Flask, render_template, request, flash
import vobject
import os
from werkzeug.utils import secure_filename
import quopri
import base64

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def decode_field(value):
    """Decode potentially encoded VCF field values"""
    try:
        # Try quoted-printable decoding
        decoded = quopri.decodestring(value.encode()).decode('utf-8', errors='ignore')
        return decoded
    except:
        try:
            # Try base64 decoding
            decoded = base64.b64decode(value).decode('utf-8', errors='ignore')
            return decoded
        except:
            # Return original if decoding fails
            return value

def parse_vcf(file_path):
    contacts = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        vcf_content = f.read()
        
        # Split content into individual vCards
        vcard_blocks = vcf_content.split('BEGIN:VCARD')
        
        for block in vcard_blocks:
            if not block.strip():
                continue
                
            try:
                vcard = vobject.readOne('BEGIN:VCARD' + block)
                contact = {
                    'full_name': decode_field(str(vcard.fn.value)) if hasattr(vcard, 'fn') else 'No Name',
                    'email': decode_field(str(vcard.email.value)) if hasattr(vcard, 'email') else '',
                    'phone': decode_field(str(vcard.tel.value)) if hasattr(vcard, 'tel') else '',
                    'organization': decode_field(str(vcard.org.value[0])) if hasattr(vcard, 'org') else '',
                    'photo': vcard.photo.value if hasattr(vcard, 'photo') else None
                }
                contacts.append(contact)
            except Exception as e:
                # Skip malformed entries but continue processing
                continue
                
    return contacts

@app.route('/', methods=['GET', 'POST'])
def index():
    contacts = []
    if request.method == 'POST':
        if 'vcf_file' not in request.files:
            flash('No file selected')
            return render_template('index.html', contacts=[])
        
        file = request.files['vcf_file']
        if file.filename == '':
            flash('No file selected')
            return render_template('index.html', contacts=[])
        
        if file and file.filename.endswith('.vcf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            try:
                contacts = parse_vcf(filepath)
                if not contacts:
                    flash('No valid contacts found in the file')
                os.remove(filepath)  # Clean up after parsing
            except Exception as e:
                flash(f'Error parsing VCF file: {str(e)}')
                contacts = []
        else:
            flash('Please upload a valid .vcf file')
            
    return render_template('index.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)