from flask import Flask, render_template, request, flash, Response
import vobject
import os
from werkzeug.utils import secure_filename
import quopri
import base64
import tempfile

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

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
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                file.save(temp_file.name)
                try:
                    contacts = parse_vcf(temp_file.name)
                    if not contacts:
                        flash('No valid contacts found in the file')
                finally:
                    # Clean up temporary file
                    os.unlink(temp_file.name)
        else:
            flash('Please upload a valid .vcf file')
            
    return render_template('index.html', contacts=contacts)

# For Vercel serverless deployment
app.debug = True