/**
 * AI Career Roadmap - Main JavaScript
 */

// ============================================
// DARK MODE
// ============================================
(function() {
    const STORAGE_KEY = 'theme';
    const DARK_CLASS = 'dark';
    
    function getTheme() {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) return saved;
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return DARK_CLASS;
        }
        return 'light';
    }
    
    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        const toggle = document.getElementById('theme-toggle');
        if (toggle) {
            toggle.querySelector('.theme-toggle-icon').textContent = theme === DARK_CLASS ? '☀️' : '🌙';
        }
        localStorage.setItem(STORAGE_KEY, theme);
    }
    
    applyTheme(getTheme());
    
    document.addEventListener('DOMContentLoaded', () => {
        const toggle = document.getElementById('theme-toggle');
        if (toggle) toggle.addEventListener('click', () => {
            applyTheme(document.documentElement.getAttribute('data-theme') === DARK_CLASS ? 'light' : DARK_CLASS);
        });
    });
    
    if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            if (!localStorage.getItem(STORAGE_KEY)) applyTheme(e.matches ? DARK_CLASS : 'light');
        });
    }
})();


// ============================================
// FORM HANDLING
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('roadmap-form');
    if (!form) return;
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const learningStyles = formData.getAll('learning_style');
        
        const data = {
            age: parseInt(formData.get('age')),
            industry: formData.get('industry'),
            level: formData.get('level'),
            goal: formData.get('goal'),
            duration: parseInt(formData.get('duration')),
            current_job: formData.get('current_job') || null,
            hours_per_day: formData.get('hours_per_day') || '3-4',
            learning_style: learningStyles.length > 0 ? learningStyles : ['video', 'reading', 'practice']
        };
        
        if (!validateForm(data)) return;
        
        showLoading();
        
        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (result.success && result.slug) {
                window.location.href = `/roadmap/${result.slug}`;
            } else {
                hideLoading();
                showError(result.error || 'Có lỗi xảy ra, vui lòng thử lại.');
            }
        } catch (error) {
            hideLoading();
            showError('Mất kết nối, kiểm tra mạng.');
        }
    });
});


function validateForm(data) {
    let isValid = true;
    document.querySelectorAll('.form-error').forEach(el => { el.style.display = 'none'; el.textContent = ''; });
    
    if (!data.age || data.age < 15 || data.age > 60) { showFieldError('age', 'Tuổi phải từ 15 đến 60'); isValid = false; }
    if (!data.industry) { showFieldError('industry', 'Vui lòng chọn ngành'); isValid = false; }
    if (!data.level) { showFieldError('level', 'Vui lòng chọn trình độ'); isValid = false; }
    if (!data.goal || data.goal.length < 10) { showFieldError('goal', 'Mục tiêu tối thiểu 10 ký tự'); isValid = false; }
    
    return isValid;
}


function showFieldError(field, message) {
    const el = document.getElementById(`${field}-error`);
    if (el) { el.textContent = message; el.style.display = 'block'; }
}


function showError(message) {
    let alert = document.getElementById('error-alert');
    if (!alert) {
        alert = document.createElement('div');
        alert.id = 'error-alert';
        alert.style.cssText = 'position:fixed;top:20px;right:20px;padding:16px 24px;background:#fee2e2;color:#991b1b;border-radius:8px;font-size:14px;z-index:10000;max-width:300px;';
        document.body.appendChild(alert);
    }
    alert.textContent = message;
    alert.style.display = 'block';
    setTimeout(() => { alert.style.display = 'none'; }, 5000);
}


// ============================================
// LOADING STATE
// ============================================
function showLoading() {
    const form = document.getElementById('roadmap-form');
    const loading = document.getElementById('loading');
    if (form) form.style.display = 'none';
    if (loading) {
        loading.style.display = 'block';
        animateLoadingStages();
    }
}

function hideLoading() {
    const form = document.getElementById('roadmap-form');
    const loading = document.getElementById('loading');
    if (form) form.style.display = 'block';
    if (loading) loading.style.display = 'none';
}

function animateLoadingStages() {
    const stages = [
        { id: 'stage-1', delay: 0 },
        { id: 'stage-2', delay: 5000 },
        { id: 'stage-3', delay: 15000 },
        { id: 'stage-4', delay: 30000 },
        { id: 'stage-5', delay: 50000 }
    ];
    stages.forEach(stage => {
        setTimeout(() => {
            stages.forEach(s => {
                const el = document.getElementById(s.id);
                if (el) {
                    el.classList.remove('active', 'done');
                    if (s.delay < stage.delay) el.classList.add('done');
                    else if (s.id === stage.id) el.classList.add('active');
                }
            });
        }, stage.delay);
    });
}


// ============================================
// ROADMAP PAGE - PHASE/MODULE TOGGLE
// ============================================
function togglePhase(phaseId) {
    const content = document.getElementById(`content-${phaseId}`);
    const toggle = document.getElementById(`toggle-${phaseId}`);
    if (content && toggle) {
        const isHidden = content.style.display === 'none';
        content.style.display = isHidden ? 'block' : 'none';
        toggle.classList.toggle('expanded', isHidden);
    }
}

function toggleModule(moduleId) {
    const content = document.getElementById(`content-${moduleId}`);
    const toggle = document.getElementById(`toggle-${moduleId}`);
    if (content && toggle) {
        const isHidden = content.style.display === 'none';
        content.style.display = isHidden ? 'block' : 'none';
        toggle.classList.toggle('expanded', isHidden);
    }
}


// ============================================
// ROADMAP PAGE - TASK & CHECKLIST
// ============================================
function toggleTask(taskId) {
    const task = document.getElementById(`task-${taskId}`);
    if (task) task.classList.toggle('completed');
    updateProgress();
    saveProgress();
}

document.addEventListener('DOMContentLoaded', () => {
    // Load saved progress
    const checkboxes = document.querySelectorAll('input[data-task-id]');
    checkboxes.forEach(cb => {
        const taskId = cb.dataset.taskId;
        if (localStorage.getItem(`task-${taskId}`) === 'true') {
            cb.checked = true;
            const task = document.getElementById(`task-${taskId}`);
            if (task) task.classList.add('completed');
        }
        cb.addEventListener('change', () => toggleTask(cb.dataset.taskId));
    });
    
    // Load saved checklists
    const checklistItems = document.querySelectorAll('input[data-checklist]');
    checklistItems.forEach(cb => {
        const key = cb.dataset.checklist;
        if (localStorage.getItem(`check-${key}`) === 'true') {
            cb.checked = true;
        }
        cb.addEventListener('change', () => {
            localStorage.setItem(`check-${key}`, cb.checked);
            updateProgress();
        });
    });
    
    updateProgress();
});


function updateProgress() {
    const total = document.querySelectorAll('input[data-task-id]').length;
    const checked = document.querySelectorAll('input[data-task-id]:checked').length;
    const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;
    
    const fill = document.getElementById('progress-fill');
    const text = document.getElementById('progress-text');
    if (fill) fill.style.width = `${percentage}%`;
    if (text) text.textContent = `${percentage}% hoàn thành (${checked}/${total} tasks)`;
}


function saveProgress() {
    // Progress is saved automatically via localStorage in toggleTask
}


// ============================================
// SHARE & FEEDBACK
// ============================================
function copyLink() {
    navigator.clipboard.writeText(window.location.href).then(() => showToast('Đã copy link!')).catch(() => {
        const input = document.createElement('input');
        input.value = window.location.href;
        document.body.appendChild(input);
        input.select();
        document.execCommand('copy');
        document.body.removeChild(input);
        showToast('Đã copy link!');
    });
}

function shareFacebook() {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(window.location.href)}`, '_blank', 'width=600,height=400');
}

function submitFeedback(isPositive) {
    console.log('Feedback:', isPositive);
    showToast(isPositive ? 'Cảm ơn bạn đã đánh giá! 🎉' : 'Cảm ơn phản hồi! Chúng mình sẽ cải thiện.');
    document.querySelectorAll('.feedback-buttons button').forEach(btn => btn.disabled = true);
}


// ============================================
// TOAST
// ============================================
function showToast(message, duration = 3000) {
    const existing = document.getElementById('toast');
    if (existing) existing.remove();
    
    const toast = document.createElement('div');
    toast.id = 'toast';
    toast.textContent = message;
    toast.style.cssText = 'position:fixed;bottom:80px;right:20px;padding:12px 24px;background:#1f2937;color:white;border-radius:8px;font-size:14px;z-index:10000;animation:slideIn 0.3s ease;';
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}


// ============================================
// ANIMATIONS
// ============================================
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
    @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }
    .task-item.completed .task-name { text-decoration: line-through; color: var(--text-tertiary); }
    .task-item.completed { opacity: 0.6; }
    .phase-toggle.expanded { transform: rotate(90deg); }
    .module-toggle.expanded { transform: rotate(90deg); }
    .phase-toggle, .module-toggle { transition: transform 0.2s; }
`;
document.head.appendChild(style);
